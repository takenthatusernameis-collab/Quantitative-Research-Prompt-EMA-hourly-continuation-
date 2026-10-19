# EMA Hourly Continuation — WLD/USDT P26_89

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.8183 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.1394 |
| gross_win_rate | 0.5332 |
| sharpe_ratio | -1.6535 |
| sortino_ratio | -0.6030 |
| max_drawdown | 0.5455 |
| cagr | -0.2469 |
| net_avg_win | 67.0719 |
| net_avg_loss | -91.9073 |
| avg_hold_time_bars | 10.4822 |
| exposure | 0.3083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
