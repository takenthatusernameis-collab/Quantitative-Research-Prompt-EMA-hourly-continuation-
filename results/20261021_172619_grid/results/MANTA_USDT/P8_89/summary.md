# EMA Hourly Continuation — MANTA/USDT P8_89

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.8039 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9773 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.8280 |
| sortino_ratio | -0.5891 |
| max_drawdown | 0.5335 |
| cagr | -0.2387 |
| net_avg_win | 81.9841 |
| net_avg_loss | -96.5314 |
| avg_hold_time_bars | 28.6196 |
| exposure | 0.6635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
