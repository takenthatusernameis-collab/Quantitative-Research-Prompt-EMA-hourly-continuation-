# EMA Hourly Continuation — CFG/USDT P8_20

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8051 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.5312 |
| sortino_ratio | -1.1554 |
| max_drawdown | 0.7412 |
| cagr | -0.4112 |
| net_avg_win | 46.6929 |
| net_avg_loss | -62.8738 |
| avg_hold_time_bars | 5.1849 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
