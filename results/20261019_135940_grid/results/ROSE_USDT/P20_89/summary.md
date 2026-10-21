# EMA Hourly Continuation — ROSE/USDT P20_89

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.6506 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -4.2866 |
| sortino_ratio | -1.6493 |
| max_drawdown | 0.8708 |
| cagr | -0.5431 |
| net_avg_win | 46.4232 |
| net_avg_loss | -61.5437 |
| avg_hold_time_bars | 12.1423 |
| exposure | 0.4112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
