# EMA Hourly Continuation — CELO/USDT P20_200

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7745 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0808 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.6325 |
| sortino_ratio | -0.4435 |
| max_drawdown | 0.4491 |
| cagr | -0.1876 |
| net_avg_win | 76.1304 |
| net_avg_loss | -98.8393 |
| avg_hold_time_bars | 39.2643 |
| exposure | 0.6521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
