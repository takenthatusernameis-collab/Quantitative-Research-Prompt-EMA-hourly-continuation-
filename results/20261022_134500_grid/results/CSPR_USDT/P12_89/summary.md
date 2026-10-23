# EMA Hourly Continuation — CSPR/USDT P12_89

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.4197 |
| net_win_rate | 0.4124 |
| gross_profit_factor | 0.7042 |
| gross_win_rate | 0.4173 |
| sharpe_ratio | -7.8021 |
| sortino_ratio | -3.4800 |
| max_drawdown | 0.9868 |
| cagr | -0.8189 |
| net_avg_win | 17.0217 |
| net_avg_loss | -28.4675 |
| avg_hold_time_bars | 10.3740 |
| exposure | 0.4791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
