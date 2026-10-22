# EMA Hourly Continuation — AIOZ/USDT P20_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6607 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -3.8683 |
| sortino_ratio | -1.4332 |
| max_drawdown | 0.8330 |
| cagr | -0.4981 |
| net_avg_win | 48.1217 |
| net_avg_loss | -67.3711 |
| avg_hold_time_bars | 13.6147 |
| exposure | 0.4289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
