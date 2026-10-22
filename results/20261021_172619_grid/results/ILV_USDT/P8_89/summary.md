# EMA Hourly Continuation — ILV/USDT P8_89

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7605 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -1.9868 |
| sortino_ratio | -0.6636 |
| max_drawdown | 0.5580 |
| cagr | -0.2647 |
| net_avg_win | 64.2164 |
| net_avg_loss | -79.3705 |
| avg_hold_time_bars | 24.5264 |
| exposure | 0.6120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
