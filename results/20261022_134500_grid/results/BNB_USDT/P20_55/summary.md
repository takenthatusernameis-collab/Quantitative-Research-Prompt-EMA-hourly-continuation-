# EMA Hourly Continuation — BNB/USDT P20_55

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.2612 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.7984 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -11.7275 |
| sortino_ratio | -5.2994 |
| max_drawdown | 0.9991 |
| cagr | -0.9394 |
| net_avg_win | 9.1743 |
| net_avg_loss | -22.6143 |
| avg_hold_time_bars | 4.9288 |
| exposure | 0.2202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
