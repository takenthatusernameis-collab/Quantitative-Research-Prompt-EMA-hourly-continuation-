# EMA Hourly Continuation — TFUEL/USDT P55_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.4319 |
| net_win_rate | 0.3735 |
| gross_profit_factor | 0.6206 |
| gross_win_rate | 0.3735 |
| sharpe_ratio | -4.9751 |
| sortino_ratio | -1.3028 |
| max_drawdown | 0.7842 |
| cagr | -0.4535 |
| net_avg_win | 46.8160 |
| net_avg_loss | -64.6361 |
| avg_hold_time_bars | 6.8147 |
| exposure | 0.1048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
