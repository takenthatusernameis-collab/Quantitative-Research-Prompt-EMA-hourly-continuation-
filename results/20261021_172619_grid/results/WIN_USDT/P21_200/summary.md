# EMA Hourly Continuation — WIN/USDT P21_200

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8174 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -0.9248 |
| sortino_ratio | -0.2214 |
| max_drawdown | 0.3345 |
| cagr | -0.0983 |
| net_avg_win | 71.6342 |
| net_avg_loss | -92.8335 |
| avg_hold_time_bars | 47.5360 |
| exposure | 0.6007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
