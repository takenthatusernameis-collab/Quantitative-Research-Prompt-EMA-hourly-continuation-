# EMA Hourly Continuation — DUSK/USDT P50_144

**Symbol:** DUSK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7693 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -1.4673 |
| sortino_ratio | -0.3927 |
| max_drawdown | 0.3852 |
| cagr | -0.1662 |
| net_avg_win | 71.9215 |
| net_avg_loss | -86.8436 |
| avg_hold_time_bars | 17.0482 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
