# EMA Hourly Continuation — APE/USDT P21_34

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1145 |
| net_profit_factor | 0.3014 |
| net_win_rate | 0.4079 |
| gross_profit_factor | 0.7333 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -11.0103 |
| sortino_ratio | -5.3087 |
| max_drawdown | 0.9988 |
| cagr | -0.9316 |
| net_avg_win | 9.2283 |
| net_avg_loss | -21.0881 |
| avg_hold_time_bars | 2.2585 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
