# EMA Hourly Continuation — ZRX/USDT P8_89

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6437 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9607 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -3.7493 |
| sortino_ratio | -1.3680 |
| max_drawdown | 0.8160 |
| cagr | -0.4809 |
| net_avg_win | 45.0196 |
| net_avg_loss | -64.3736 |
| avg_hold_time_bars | 21.2678 |
| exposure | 0.6535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
