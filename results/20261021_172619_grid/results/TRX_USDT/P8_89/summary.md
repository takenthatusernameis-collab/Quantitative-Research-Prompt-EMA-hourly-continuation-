# EMA Hourly Continuation — TRX/USDT P8_89

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9998 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -3.7110 |
| sortino_ratio | -1.1728 |
| max_drawdown | 0.7544 |
| cagr | -0.4184 |
| net_avg_win | 46.4858 |
| net_avg_loss | -77.5361 |
| avg_hold_time_bars | 27.6273 |
| exposure | 0.6065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
