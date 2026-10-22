# EMA Hourly Continuation — IOST/USDT P12_200

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.9231 |
| net_win_rate | 0.5347 |
| gross_profit_factor | 1.1363 |
| gross_win_rate | 0.5347 |
| sharpe_ratio | -0.3720 |
| sortino_ratio | -0.0911 |
| max_drawdown | 0.2146 |
| cagr | -0.0447 |
| net_avg_win | 84.5492 |
| net_avg_loss | -105.2625 |
| avg_hold_time_bars | 57.8819 |
| exposure | 0.7577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
