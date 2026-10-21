# EMA Hourly Continuation — IO/USDT P8_200

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8027 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -1.8428 |
| sortino_ratio | -0.4392 |
| max_drawdown | 0.4017 |
| cagr | -0.1836 |
| net_avg_win | 75.7798 |
| net_avg_loss | -86.6122 |
| avg_hold_time_bars | 61.5393 |
| exposure | 0.7955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
