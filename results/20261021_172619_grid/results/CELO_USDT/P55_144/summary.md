# EMA Hourly Continuation — CELO/USDT P55_144

**Symbol:** CELO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.8569 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.1002 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -0.8908 |
| sortino_ratio | -0.2334 |
| max_drawdown | 0.2775 |
| cagr | -0.1035 |
| net_avg_win | 82.9253 |
| net_avg_loss | -105.8985 |
| avg_hold_time_bars | 15.9069 |
| exposure | 0.2397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
