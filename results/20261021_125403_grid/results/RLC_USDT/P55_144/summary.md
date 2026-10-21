# EMA Hourly Continuation — RLC/USDT P55_144

**Symbol:** RLC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7713 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.5217 |
| sortino_ratio | -0.4230 |
| max_drawdown | 0.4219 |
| cagr | -0.1775 |
| net_avg_win | 69.1876 |
| net_avg_loss | -90.6655 |
| avg_hold_time_bars | 13.3883 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
