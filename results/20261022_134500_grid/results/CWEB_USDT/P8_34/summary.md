# EMA Hourly Continuation — CWEB/USDT P8_34

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.4159 |
| net_win_rate | 0.3237 |
| gross_profit_factor | 0.8156 |
| gross_win_rate | 0.3398 |
| sharpe_ratio | -14.1532 |
| sortino_ratio | -6.9437 |
| max_drawdown | 0.9999 |
| cagr | -0.9761 |
| net_avg_win | 18.6848 |
| net_avg_loss | -21.5051 |
| avg_hold_time_bars | 8.1359 |
| exposure | 0.4353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
