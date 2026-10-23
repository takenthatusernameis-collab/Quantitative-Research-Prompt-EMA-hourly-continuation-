# EMA Hourly Continuation — ZETA/USDT P34_144

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7151 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 1.0280 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.7781 |
| sortino_ratio | -0.8222 |
| max_drawdown | 0.6969 |
| cagr | -0.3272 |
| net_avg_win | 73.4540 |
| net_avg_loss | -95.6303 |
| avg_hold_time_bars | 21.3326 |
| exposure | 0.4325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
