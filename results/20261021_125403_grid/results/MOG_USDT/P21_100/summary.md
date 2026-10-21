# EMA Hourly Continuation — MOG/USDT P21_100

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8239 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9606 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.2890 |
| sortino_ratio | -0.3879 |
| max_drawdown | 0.4142 |
| cagr | -0.1652 |
| net_avg_win | 79.3770 |
| net_avg_loss | -93.5387 |
| avg_hold_time_bars | 19.4409 |
| exposure | 0.3924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
