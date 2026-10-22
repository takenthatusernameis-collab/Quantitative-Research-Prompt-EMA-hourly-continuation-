# EMA Hourly Continuation — BSV/USDT P21_26

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1318 |
| net_profit_factor | 0.1237 |
| net_win_rate | 0.3088 |
| gross_profit_factor | 0.5461 |
| gross_win_rate | 0.3915 |
| sharpe_ratio | -17.7421 |
| sortino_ratio | -9.6615 |
| max_drawdown | 1.0000 |
| cagr | -0.9950 |
| net_avg_win | 3.4696 |
| net_avg_loss | -12.5270 |
| avg_hold_time_bars | 1.9954 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
