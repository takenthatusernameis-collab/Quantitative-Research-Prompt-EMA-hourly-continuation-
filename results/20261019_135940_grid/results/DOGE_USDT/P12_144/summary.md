# EMA Hourly Continuation — DOGE/USDT P12_144

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -4.2566 |
| sortino_ratio | -1.3239 |
| max_drawdown | 0.8186 |
| cagr | -0.4792 |
| net_avg_win | 45.5673 |
| net_avg_loss | -67.4013 |
| avg_hold_time_bars | 28.8200 |
| exposure | 0.6550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
