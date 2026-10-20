# EMA Hourly Continuation — ID/USDT P8_89

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6874 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.0816 |
| sortino_ratio | -1.0993 |
| max_drawdown | 0.7361 |
| cagr | -0.4038 |
| net_avg_win | 51.8594 |
| net_avg_loss | -70.6394 |
| avg_hold_time_bars | 22.8858 |
| exposure | 0.6618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
