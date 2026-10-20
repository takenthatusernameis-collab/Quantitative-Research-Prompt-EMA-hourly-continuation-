# EMA Hourly Continuation — XNO/USDT P21_55

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.4494 |
| net_win_rate | 0.3900 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -10.0745 |
| sortino_ratio | -4.7876 |
| max_drawdown | 0.9975 |
| cagr | -0.9058 |
| net_avg_win | 18.5880 |
| net_avg_loss | -26.4453 |
| avg_hold_time_bars | 4.2867 |
| exposure | 0.2188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
