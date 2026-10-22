# EMA Hourly Continuation — SKY/USDT P26_34

**Symbol:** SKY/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.2614 |
| net_win_rate | 0.3831 |
| gross_profit_factor | 0.7631 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -12.4752 |
| sortino_ratio | -5.9448 |
| max_drawdown | 0.9982 |
| cagr | -0.9543 |
| net_avg_win | 10.3582 |
| net_avg_loss | -24.6158 |
| avg_hold_time_bars | 2.4730 |
| exposure | 0.1227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
