# EMA Hourly Continuation — CFX/USDT P34_89

**Symbol:** CFX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5039 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.7857 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -5.3029 |
| sortino_ratio | -1.9325 |
| max_drawdown | 0.9051 |
| cagr | -0.6053 |
| net_avg_win | 30.4736 |
| net_avg_loss | -49.6029 |
| avg_hold_time_bars | 8.4057 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
