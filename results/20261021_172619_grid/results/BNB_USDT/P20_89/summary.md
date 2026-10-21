# EMA Hourly Continuation — BNB/USDT P20_89

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0365 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -3.1773 |
| sortino_ratio | -0.9981 |
| max_drawdown | 0.6872 |
| cagr | -0.3663 |
| net_avg_win | 47.5805 |
| net_avg_loss | -78.5520 |
| avg_hold_time_bars | 15.3375 |
| exposure | 0.3325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
