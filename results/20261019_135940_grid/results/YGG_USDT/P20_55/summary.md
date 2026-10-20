# EMA Hourly Continuation — YGG/USDT P20_55

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -5.9667 |
| sortino_ratio | -2.5650 |
| max_drawdown | 0.9586 |
| cagr | -0.7154 |
| net_avg_win | 28.4543 |
| net_avg_loss | -43.5301 |
| avg_hold_time_bars | 5.7624 |
| exposure | 0.2480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
