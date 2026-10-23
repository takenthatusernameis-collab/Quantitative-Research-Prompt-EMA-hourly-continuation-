# EMA Hourly Continuation — MTL/USDT P12_200

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8388 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.1318 |
| gross_win_rate | 0.5321 |
| sharpe_ratio | -0.8639 |
| sortino_ratio | -0.2054 |
| max_drawdown | 0.2503 |
| cagr | -0.0936 |
| net_avg_win | 77.2099 |
| net_avg_loss | -103.1994 |
| avg_hold_time_bars | 63.4393 |
| exposure | 0.8038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
