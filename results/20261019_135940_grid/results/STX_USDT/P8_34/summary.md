# EMA Hourly Continuation — STX/USDT P8_34

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1373 |
| net_profit_factor | 0.4980 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -8.4515 |
| sortino_ratio | -4.3851 |
| max_drawdown | 0.9960 |
| cagr | -0.8844 |
| net_avg_win | 16.0879 |
| net_avg_loss | -26.1327 |
| avg_hold_time_bars | 5.4465 |
| exposure | 0.3384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
