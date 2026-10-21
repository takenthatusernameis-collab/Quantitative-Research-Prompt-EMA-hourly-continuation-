# EMA Hourly Continuation — AR/USDT P20_21

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.6179 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8544 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -1.6819 |
| sortino_ratio | -0.2606 |
| max_drawdown | 0.2745 |
| cagr | -0.1135 |
| net_avg_win | 78.1615 |
| net_avg_loss | -106.7259 |
| avg_hold_time_bars | 5.7203 |
| exposure | 0.0307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
