# EMA Hourly Continuation — ARB/USDT P34_55

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.4046 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8678 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -7.4241 |
| sortino_ratio | -3.0407 |
| max_drawdown | 0.9786 |
| cagr | -0.7835 |
| net_avg_win | 17.4980 |
| net_avg_loss | -35.4198 |
| avg_hold_time_bars | 3.3874 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
