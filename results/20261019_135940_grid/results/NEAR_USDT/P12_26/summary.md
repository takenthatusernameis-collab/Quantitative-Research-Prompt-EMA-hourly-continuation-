# EMA Hourly Continuation — NEAR/USDT P12_26

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1443 |
| net_profit_factor | 0.4267 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.8432 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -10.8685 |
| sortino_ratio | -5.8059 |
| max_drawdown | 0.9994 |
| cagr | -0.9476 |
| net_avg_win | 11.9790 |
| net_avg_loss | -21.2079 |
| avg_hold_time_bars | 2.6985 |
| exposure | 0.1770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
