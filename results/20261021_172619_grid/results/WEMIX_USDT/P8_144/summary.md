# EMA Hourly Continuation — WEMIX/USDT P8_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.5251 |
| net_win_rate | 0.3835 |
| gross_profit_factor | 0.6430 |
| gross_win_rate | 0.3835 |
| sharpe_ratio | -4.4498 |
| sortino_ratio | -1.2897 |
| max_drawdown | 0.7874 |
| cagr | -0.4519 |
| net_avg_win | 52.8441 |
| net_avg_loss | -62.6115 |
| avg_hold_time_bars | 37.3506 |
| exposure | 0.7215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
