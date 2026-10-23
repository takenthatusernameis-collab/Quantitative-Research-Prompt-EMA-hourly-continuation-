# EMA Hourly Continuation — TRADE/USDT P20_200

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7351 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9236 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.7128 |
| sortino_ratio | -0.4445 |
| max_drawdown | 0.4174 |
| cagr | -0.1874 |
| net_avg_win | 70.8883 |
| net_avg_loss | -86.6212 |
| avg_hold_time_bars | 38.7530 |
| exposure | 0.5919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
