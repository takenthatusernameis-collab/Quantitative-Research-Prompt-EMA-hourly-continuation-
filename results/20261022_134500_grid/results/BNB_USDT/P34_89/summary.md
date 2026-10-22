# EMA Hourly Continuation — BNB/USDT P34_89

**Symbol:** BNB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.3217 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -8.4766 |
| sortino_ratio | -3.2206 |
| max_drawdown | 0.9849 |
| cagr | -0.8098 |
| net_avg_win | 15.3072 |
| net_avg_loss | -35.4864 |
| avg_hold_time_bars | 6.6401 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
