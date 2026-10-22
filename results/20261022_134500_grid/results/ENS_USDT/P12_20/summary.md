# EMA Hourly Continuation — ENS/USDT P12_20

**Symbol:** ENS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1526 |
| net_profit_factor | 0.3951 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.8675 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -14.1206 |
| sortino_ratio | -7.8832 |
| max_drawdown | 1.0000 |
| cagr | -0.9830 |
| net_avg_win | 10.8482 |
| net_avg_loss | -17.8899 |
| avg_hold_time_bars | 2.3840 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
