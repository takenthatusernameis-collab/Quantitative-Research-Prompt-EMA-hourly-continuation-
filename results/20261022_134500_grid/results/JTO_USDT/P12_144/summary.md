# EMA Hourly Continuation — JTO/USDT P12_144

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7830 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.7361 |
| sortino_ratio | -0.5494 |
| max_drawdown | 0.5313 |
| cagr | -0.2274 |
| net_avg_win | 68.8517 |
| net_avg_loss | -88.6373 |
| avg_hold_time_bars | 29.3153 |
| exposure | 0.6636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
