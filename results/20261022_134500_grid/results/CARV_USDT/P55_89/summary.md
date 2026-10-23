# EMA Hourly Continuation — CARV/USDT P55_89

**Symbol:** CARV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.4304 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -5.8005 |
| sortino_ratio | -1.9118 |
| max_drawdown | 0.8491 |
| cagr | -0.5965 |
| net_avg_win | 34.3635 |
| net_avg_loss | -59.5584 |
| avg_hold_time_bars | 4.9076 |
| exposure | 0.1196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
