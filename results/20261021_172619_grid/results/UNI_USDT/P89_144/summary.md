# EMA Hourly Continuation — UNI/USDT P89_144

**Symbol:** UNI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.8483 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.0992 |
| gross_win_rate | 0.5252 |
| sharpe_ratio | -0.7603 |
| sortino_ratio | -0.1692 |
| max_drawdown | 0.2437 |
| cagr | -0.0761 |
| net_avg_win | 80.5849 |
| net_avg_loss | -105.0884 |
| avg_hold_time_bars | 9.2101 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
