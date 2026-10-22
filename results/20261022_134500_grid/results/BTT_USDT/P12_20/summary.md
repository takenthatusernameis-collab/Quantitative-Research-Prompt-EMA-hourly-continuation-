# EMA Hourly Continuation — BTT/USDT P12_20

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1583 |
| net_profit_factor | 0.1230 |
| net_win_rate | 0.2521 |
| gross_profit_factor | 0.5753 |
| gross_win_rate | 0.3563 |
| sharpe_ratio | -22.9307 |
| sortino_ratio | -14.3915 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 3.5140 |
| net_avg_loss | -9.6301 |
| avg_hold_time_bars | 2.3272 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
