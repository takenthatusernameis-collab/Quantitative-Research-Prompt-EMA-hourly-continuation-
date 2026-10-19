# EMA Hourly Continuation — STX/USDT P12_89

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9293 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -3.4999 |
| sortino_ratio | -1.2807 |
| max_drawdown | 0.8055 |
| cagr | -0.4522 |
| net_avg_win | 44.3401 |
| net_avg_loss | -63.9065 |
| avg_hold_time_bars | 18.9955 |
| exposure | 0.5768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
