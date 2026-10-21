# EMA Hourly Continuation — WLD/USDT P12_34

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.8275 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0400 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.4501 |
| sortino_ratio | -0.4862 |
| max_drawdown | 0.5255 |
| cagr | -0.2016 |
| net_avg_win | 74.7795 |
| net_avg_loss | -93.4055 |
| avg_hold_time_bars | 7.0642 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
