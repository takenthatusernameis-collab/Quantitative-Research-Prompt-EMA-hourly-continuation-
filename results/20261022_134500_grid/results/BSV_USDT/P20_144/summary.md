# EMA Hourly Continuation — BSV/USDT P20_144

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.8082 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -5.2651 |
| sortino_ratio | -1.7773 |
| max_drawdown | 0.8884 |
| cagr | -0.5781 |
| net_avg_win | 36.7130 |
| net_avg_loss | -53.5608 |
| avg_hold_time_bars | 20.4872 |
| exposure | 0.5448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
