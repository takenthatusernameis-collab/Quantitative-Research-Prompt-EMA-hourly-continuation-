# EMA Hourly Continuation — BONK/USDT P12_89

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.9280 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0880 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -0.4643 |
| sortino_ratio | -0.1426 |
| max_drawdown | 0.2769 |
| cagr | -0.0693 |
| net_avg_win | 89.4143 |
| net_avg_loss | -105.1909 |
| avg_hold_time_bars | 26.2061 |
| exposure | 0.5432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
