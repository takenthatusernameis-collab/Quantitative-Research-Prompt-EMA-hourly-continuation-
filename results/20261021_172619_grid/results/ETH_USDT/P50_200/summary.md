# EMA Hourly Continuation — ETH/USDT P50_200

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -1.9420 |
| sortino_ratio | -0.4416 |
| max_drawdown | 0.4213 |
| cagr | -0.1831 |
| net_avg_win | 63.8091 |
| net_avg_loss | -91.0082 |
| avg_hold_time_bars | 34.7312 |
| exposure | 0.3994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
