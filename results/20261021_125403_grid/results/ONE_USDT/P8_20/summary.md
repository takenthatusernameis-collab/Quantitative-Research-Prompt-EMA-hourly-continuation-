# EMA Hourly Continuation — ONE/USDT P8_20

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.8052 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0779 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -1.5389 |
| sortino_ratio | -0.5071 |
| max_drawdown | 0.4586 |
| cagr | -0.2081 |
| net_avg_win | 67.6048 |
| net_avg_loss | -90.2947 |
| avg_hold_time_bars | 5.0229 |
| exposure | 0.1194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
