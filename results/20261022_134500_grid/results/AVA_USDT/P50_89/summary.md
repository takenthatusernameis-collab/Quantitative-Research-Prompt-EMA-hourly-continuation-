# EMA Hourly Continuation — AVA/USDT P50_89

**Symbol:** AVA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.5370 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9960 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -4.9820 |
| sortino_ratio | -1.8495 |
| max_drawdown | 0.9013 |
| cagr | -0.5956 |
| net_avg_win | 30.5152 |
| net_avg_loss | -54.5813 |
| avg_hold_time_bars | 4.0647 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
