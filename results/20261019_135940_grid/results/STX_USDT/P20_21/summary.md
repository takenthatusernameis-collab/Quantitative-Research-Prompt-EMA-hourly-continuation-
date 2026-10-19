# EMA Hourly Continuation — STX/USDT P20_21

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1175 |
| net_profit_factor | 0.1427 |
| net_win_rate | 0.3064 |
| gross_profit_factor | 0.5618 |
| gross_win_rate | 0.3779 |
| sharpe_ratio | -17.2501 |
| sortino_ratio | -8.9204 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 4.6251 |
| net_avg_loss | -14.3129 |
| avg_hold_time_bars | 1.6587 |
| exposure | 0.0882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
