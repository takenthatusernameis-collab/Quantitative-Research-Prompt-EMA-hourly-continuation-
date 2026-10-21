# EMA Hourly Continuation — KNC/USDT P12_55

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6835 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -3.8690 |
| sortino_ratio | -1.4342 |
| max_drawdown | 0.8170 |
| cagr | -0.4831 |
| net_avg_win | 55.1299 |
| net_avg_loss | -71.4241 |
| avg_hold_time_bars | 13.8148 |
| exposure | 0.4239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
