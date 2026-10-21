# EMA Hourly Continuation — ZETA/USDT P34_144

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8265 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9993 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.1858 |
| sortino_ratio | -0.3096 |
| max_drawdown | 0.3944 |
| cagr | -0.1346 |
| net_avg_win | 87.6973 |
| net_avg_loss | -104.2180 |
| avg_hold_time_bars | 27.8806 |
| exposure | 0.4226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
