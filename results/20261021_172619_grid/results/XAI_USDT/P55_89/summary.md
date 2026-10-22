# EMA Hourly Continuation — XAI/USDT P55_89

**Symbol:** XAI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6711 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -2.5125 |
| sortino_ratio | -0.6881 |
| max_drawdown | 0.5728 |
| cagr | -0.2710 |
| net_avg_win | 64.6229 |
| net_avg_loss | -85.4294 |
| avg_hold_time_bars | 6.4755 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
