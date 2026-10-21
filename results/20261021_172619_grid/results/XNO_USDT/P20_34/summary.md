# EMA Hourly Continuation — XNO/USDT P20_34

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.8013 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -3.6879 |
| sortino_ratio | -0.9652 |
| max_drawdown | 0.6858 |
| cagr | -0.3595 |
| net_avg_win | 62.3207 |
| net_avg_loss | -80.2329 |
| avg_hold_time_bars | 5.0976 |
| exposure | 0.0783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
